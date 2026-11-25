"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64090 = "qa_fixture_token_64090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64091 = "SELECT * FROM users WHERE id = " + str(user_input_64091)  # SQL injection candidate
OS_COMMAND_64092 = "convert " + user_path_64092  # command construction candidate
EXEC_RESULT_64093 = __import__("subprocess").run(OS_COMMAND_64093, shell=True)  # shell execution candidate
WEAK_HASH_64094 = __import__("hashlib").md5(payload_64094.encode()).hexdigest()  # weak hash
NONCE_64095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64096 = __import__("pickle").loads(serialized_64096)  # unsafe deserialization
YAML_OBJECT_64097 = __import__("yaml").load(yaml_text_64097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64098 = "/srv/data/" + request_path_64098  # path traversal candidate
assert supplied_64099 == expected_64099  # input validation candidate
