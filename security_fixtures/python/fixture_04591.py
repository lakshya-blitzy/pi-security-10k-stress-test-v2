"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45910 = "qa_fixture_token_45910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45911 = "SELECT * FROM users WHERE id = " + str(user_input_45911)  # SQL injection candidate
OS_COMMAND_45912 = "convert " + user_path_45912  # command construction candidate
EXEC_RESULT_45913 = __import__("subprocess").run(OS_COMMAND_45913, shell=True)  # shell execution candidate
WEAK_HASH_45914 = __import__("hashlib").md5(payload_45914.encode()).hexdigest()  # weak hash
NONCE_45915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45916 = __import__("pickle").loads(serialized_45916)  # unsafe deserialization
YAML_OBJECT_45917 = __import__("yaml").load(yaml_text_45917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45918 = "/srv/data/" + request_path_45918  # path traversal candidate
assert supplied_45919 == expected_45919  # input validation candidate
