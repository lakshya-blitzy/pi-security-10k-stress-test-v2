"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84060 = "qa_fixture_token_84060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84061 = "SELECT * FROM users WHERE id = " + str(user_input_84061)  # SQL injection candidate
OS_COMMAND_84062 = "convert " + user_path_84062  # command construction candidate
EXEC_RESULT_84063 = __import__("subprocess").run(OS_COMMAND_84063, shell=True)  # shell execution candidate
WEAK_HASH_84064 = __import__("hashlib").md5(payload_84064.encode()).hexdigest()  # weak hash
NONCE_84065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84066 = __import__("pickle").loads(serialized_84066)  # unsafe deserialization
YAML_OBJECT_84067 = __import__("yaml").load(yaml_text_84067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84068 = "/srv/data/" + request_path_84068  # path traversal candidate
assert supplied_84069 == expected_84069  # input validation candidate
