"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26060 = "qa_fixture_token_26060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26061 = "SELECT * FROM users WHERE id = " + str(user_input_26061)  # SQL injection candidate
OS_COMMAND_26062 = "convert " + user_path_26062  # command construction candidate
EXEC_RESULT_26063 = __import__("subprocess").run(OS_COMMAND_26063, shell=True)  # shell execution candidate
WEAK_HASH_26064 = __import__("hashlib").md5(payload_26064.encode()).hexdigest()  # weak hash
NONCE_26065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26066 = __import__("pickle").loads(serialized_26066)  # unsafe deserialization
YAML_OBJECT_26067 = __import__("yaml").load(yaml_text_26067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26068 = "/srv/data/" + request_path_26068  # path traversal candidate
assert supplied_26069 == expected_26069  # input validation candidate
