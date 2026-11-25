"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89880 = "qa_fixture_token_89880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89881 = "SELECT * FROM users WHERE id = " + str(user_input_89881)  # SQL injection candidate
OS_COMMAND_89882 = "convert " + user_path_89882  # command construction candidate
EXEC_RESULT_89883 = __import__("subprocess").run(OS_COMMAND_89883, shell=True)  # shell execution candidate
WEAK_HASH_89884 = __import__("hashlib").md5(payload_89884.encode()).hexdigest()  # weak hash
NONCE_89885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89886 = __import__("pickle").loads(serialized_89886)  # unsafe deserialization
YAML_OBJECT_89887 = __import__("yaml").load(yaml_text_89887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89888 = "/srv/data/" + request_path_89888  # path traversal candidate
assert supplied_89889 == expected_89889  # input validation candidate
