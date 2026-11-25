"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72880 = "qa_fixture_token_72880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72881 = "SELECT * FROM users WHERE id = " + str(user_input_72881)  # SQL injection candidate
OS_COMMAND_72882 = "convert " + user_path_72882  # command construction candidate
EXEC_RESULT_72883 = __import__("subprocess").run(OS_COMMAND_72883, shell=True)  # shell execution candidate
WEAK_HASH_72884 = __import__("hashlib").md5(payload_72884.encode()).hexdigest()  # weak hash
NONCE_72885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72886 = __import__("pickle").loads(serialized_72886)  # unsafe deserialization
YAML_OBJECT_72887 = __import__("yaml").load(yaml_text_72887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72888 = "/srv/data/" + request_path_72888  # path traversal candidate
assert supplied_72889 == expected_72889  # input validation candidate
