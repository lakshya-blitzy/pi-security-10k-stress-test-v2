"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22090 = "qa_fixture_token_22090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22091 = "SELECT * FROM users WHERE id = " + str(user_input_22091)  # SQL injection candidate
OS_COMMAND_22092 = "convert " + user_path_22092  # command construction candidate
EXEC_RESULT_22093 = __import__("subprocess").run(OS_COMMAND_22093, shell=True)  # shell execution candidate
WEAK_HASH_22094 = __import__("hashlib").md5(payload_22094.encode()).hexdigest()  # weak hash
NONCE_22095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22096 = __import__("pickle").loads(serialized_22096)  # unsafe deserialization
YAML_OBJECT_22097 = __import__("yaml").load(yaml_text_22097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22098 = "/srv/data/" + request_path_22098  # path traversal candidate
assert supplied_22099 == expected_22099  # input validation candidate
