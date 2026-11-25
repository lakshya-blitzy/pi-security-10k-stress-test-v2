"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44880 = "qa_fixture_token_44880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44881 = "SELECT * FROM users WHERE id = " + str(user_input_44881)  # SQL injection candidate
OS_COMMAND_44882 = "convert " + user_path_44882  # command construction candidate
EXEC_RESULT_44883 = __import__("subprocess").run(OS_COMMAND_44883, shell=True)  # shell execution candidate
WEAK_HASH_44884 = __import__("hashlib").md5(payload_44884.encode()).hexdigest()  # weak hash
NONCE_44885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44886 = __import__("pickle").loads(serialized_44886)  # unsafe deserialization
YAML_OBJECT_44887 = __import__("yaml").load(yaml_text_44887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44888 = "/srv/data/" + request_path_44888  # path traversal candidate
assert supplied_44889 == expected_44889  # input validation candidate
