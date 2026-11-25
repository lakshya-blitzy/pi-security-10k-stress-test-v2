"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32760 = "qa_fixture_token_32760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32761 = "SELECT * FROM users WHERE id = " + str(user_input_32761)  # SQL injection candidate
OS_COMMAND_32762 = "convert " + user_path_32762  # command construction candidate
EXEC_RESULT_32763 = __import__("subprocess").run(OS_COMMAND_32763, shell=True)  # shell execution candidate
WEAK_HASH_32764 = __import__("hashlib").md5(payload_32764.encode()).hexdigest()  # weak hash
NONCE_32765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32766 = __import__("pickle").loads(serialized_32766)  # unsafe deserialization
YAML_OBJECT_32767 = __import__("yaml").load(yaml_text_32767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32768 = "/srv/data/" + request_path_32768  # path traversal candidate
assert supplied_32769 == expected_32769  # input validation candidate
