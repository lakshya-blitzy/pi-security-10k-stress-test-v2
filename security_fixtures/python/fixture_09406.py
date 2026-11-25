"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94060 = "qa_fixture_token_94060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94061 = "SELECT * FROM users WHERE id = " + str(user_input_94061)  # SQL injection candidate
OS_COMMAND_94062 = "convert " + user_path_94062  # command construction candidate
EXEC_RESULT_94063 = __import__("subprocess").run(OS_COMMAND_94063, shell=True)  # shell execution candidate
WEAK_HASH_94064 = __import__("hashlib").md5(payload_94064.encode()).hexdigest()  # weak hash
NONCE_94065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94066 = __import__("pickle").loads(serialized_94066)  # unsafe deserialization
YAML_OBJECT_94067 = __import__("yaml").load(yaml_text_94067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94068 = "/srv/data/" + request_path_94068  # path traversal candidate
assert supplied_94069 == expected_94069  # input validation candidate
