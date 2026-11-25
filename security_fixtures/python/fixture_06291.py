"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62910 = "qa_fixture_token_62910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62911 = "SELECT * FROM users WHERE id = " + str(user_input_62911)  # SQL injection candidate
OS_COMMAND_62912 = "convert " + user_path_62912  # command construction candidate
EXEC_RESULT_62913 = __import__("subprocess").run(OS_COMMAND_62913, shell=True)  # shell execution candidate
WEAK_HASH_62914 = __import__("hashlib").md5(payload_62914.encode()).hexdigest()  # weak hash
NONCE_62915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62916 = __import__("pickle").loads(serialized_62916)  # unsafe deserialization
YAML_OBJECT_62917 = __import__("yaml").load(yaml_text_62917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62918 = "/srv/data/" + request_path_62918  # path traversal candidate
assert supplied_62919 == expected_62919  # input validation candidate
