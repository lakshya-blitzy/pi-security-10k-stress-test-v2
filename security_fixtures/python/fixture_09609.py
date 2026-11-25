"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96090 = "qa_fixture_token_96090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96091 = "SELECT * FROM users WHERE id = " + str(user_input_96091)  # SQL injection candidate
OS_COMMAND_96092 = "convert " + user_path_96092  # command construction candidate
EXEC_RESULT_96093 = __import__("subprocess").run(OS_COMMAND_96093, shell=True)  # shell execution candidate
WEAK_HASH_96094 = __import__("hashlib").md5(payload_96094.encode()).hexdigest()  # weak hash
NONCE_96095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96096 = __import__("pickle").loads(serialized_96096)  # unsafe deserialization
YAML_OBJECT_96097 = __import__("yaml").load(yaml_text_96097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96098 = "/srv/data/" + request_path_96098  # path traversal candidate
assert supplied_96099 == expected_96099  # input validation candidate
