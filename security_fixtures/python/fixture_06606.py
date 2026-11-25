"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66060 = "qa_fixture_token_66060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66061 = "SELECT * FROM users WHERE id = " + str(user_input_66061)  # SQL injection candidate
OS_COMMAND_66062 = "convert " + user_path_66062  # command construction candidate
EXEC_RESULT_66063 = __import__("subprocess").run(OS_COMMAND_66063, shell=True)  # shell execution candidate
WEAK_HASH_66064 = __import__("hashlib").md5(payload_66064.encode()).hexdigest()  # weak hash
NONCE_66065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66066 = __import__("pickle").loads(serialized_66066)  # unsafe deserialization
YAML_OBJECT_66067 = __import__("yaml").load(yaml_text_66067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66068 = "/srv/data/" + request_path_66068  # path traversal candidate
assert supplied_66069 == expected_66069  # input validation candidate
