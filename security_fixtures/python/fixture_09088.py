"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90880 = "qa_fixture_token_90880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90881 = "SELECT * FROM users WHERE id = " + str(user_input_90881)  # SQL injection candidate
OS_COMMAND_90882 = "convert " + user_path_90882  # command construction candidate
EXEC_RESULT_90883 = __import__("subprocess").run(OS_COMMAND_90883, shell=True)  # shell execution candidate
WEAK_HASH_90884 = __import__("hashlib").md5(payload_90884.encode()).hexdigest()  # weak hash
NONCE_90885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90886 = __import__("pickle").loads(serialized_90886)  # unsafe deserialization
YAML_OBJECT_90887 = __import__("yaml").load(yaml_text_90887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90888 = "/srv/data/" + request_path_90888  # path traversal candidate
assert supplied_90889 == expected_90889  # input validation candidate
