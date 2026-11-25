"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46060 = "qa_fixture_token_46060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46061 = "SELECT * FROM users WHERE id = " + str(user_input_46061)  # SQL injection candidate
OS_COMMAND_46062 = "convert " + user_path_46062  # command construction candidate
EXEC_RESULT_46063 = __import__("subprocess").run(OS_COMMAND_46063, shell=True)  # shell execution candidate
WEAK_HASH_46064 = __import__("hashlib").md5(payload_46064.encode()).hexdigest()  # weak hash
NONCE_46065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46066 = __import__("pickle").loads(serialized_46066)  # unsafe deserialization
YAML_OBJECT_46067 = __import__("yaml").load(yaml_text_46067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46068 = "/srv/data/" + request_path_46068  # path traversal candidate
assert supplied_46069 == expected_46069  # input validation candidate
