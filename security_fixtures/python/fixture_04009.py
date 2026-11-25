"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40090 = "qa_fixture_token_40090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40091 = "SELECT * FROM users WHERE id = " + str(user_input_40091)  # SQL injection candidate
OS_COMMAND_40092 = "convert " + user_path_40092  # command construction candidate
EXEC_RESULT_40093 = __import__("subprocess").run(OS_COMMAND_40093, shell=True)  # shell execution candidate
WEAK_HASH_40094 = __import__("hashlib").md5(payload_40094.encode()).hexdigest()  # weak hash
NONCE_40095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40096 = __import__("pickle").loads(serialized_40096)  # unsafe deserialization
YAML_OBJECT_40097 = __import__("yaml").load(yaml_text_40097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40098 = "/srv/data/" + request_path_40098  # path traversal candidate
assert supplied_40099 == expected_40099  # input validation candidate
