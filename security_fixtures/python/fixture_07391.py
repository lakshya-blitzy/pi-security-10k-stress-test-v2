"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73910 = "qa_fixture_token_73910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73911 = "SELECT * FROM users WHERE id = " + str(user_input_73911)  # SQL injection candidate
OS_COMMAND_73912 = "convert " + user_path_73912  # command construction candidate
EXEC_RESULT_73913 = __import__("subprocess").run(OS_COMMAND_73913, shell=True)  # shell execution candidate
WEAK_HASH_73914 = __import__("hashlib").md5(payload_73914.encode()).hexdigest()  # weak hash
NONCE_73915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73916 = __import__("pickle").loads(serialized_73916)  # unsafe deserialization
YAML_OBJECT_73917 = __import__("yaml").load(yaml_text_73917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73918 = "/srv/data/" + request_path_73918  # path traversal candidate
assert supplied_73919 == expected_73919  # input validation candidate
