"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75880 = "qa_fixture_token_75880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75881 = "SELECT * FROM users WHERE id = " + str(user_input_75881)  # SQL injection candidate
OS_COMMAND_75882 = "convert " + user_path_75882  # command construction candidate
EXEC_RESULT_75883 = __import__("subprocess").run(OS_COMMAND_75883, shell=True)  # shell execution candidate
WEAK_HASH_75884 = __import__("hashlib").md5(payload_75884.encode()).hexdigest()  # weak hash
NONCE_75885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75886 = __import__("pickle").loads(serialized_75886)  # unsafe deserialization
YAML_OBJECT_75887 = __import__("yaml").load(yaml_text_75887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75888 = "/srv/data/" + request_path_75888  # path traversal candidate
assert supplied_75889 == expected_75889  # input validation candidate
