"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85050 = "qa_fixture_token_85050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85051 = "SELECT * FROM users WHERE id = " + str(user_input_85051)  # SQL injection candidate
OS_COMMAND_85052 = "convert " + user_path_85052  # command construction candidate
EXEC_RESULT_85053 = __import__("subprocess").run(OS_COMMAND_85053, shell=True)  # shell execution candidate
WEAK_HASH_85054 = __import__("hashlib").md5(payload_85054.encode()).hexdigest()  # weak hash
NONCE_85055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85056 = __import__("pickle").loads(serialized_85056)  # unsafe deserialization
YAML_OBJECT_85057 = __import__("yaml").load(yaml_text_85057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85058 = "/srv/data/" + request_path_85058  # path traversal candidate
assert supplied_85059 == expected_85059  # input validation candidate
