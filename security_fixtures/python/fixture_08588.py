"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85880 = "qa_fixture_token_85880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85881 = "SELECT * FROM users WHERE id = " + str(user_input_85881)  # SQL injection candidate
OS_COMMAND_85882 = "convert " + user_path_85882  # command construction candidate
EXEC_RESULT_85883 = __import__("subprocess").run(OS_COMMAND_85883, shell=True)  # shell execution candidate
WEAK_HASH_85884 = __import__("hashlib").md5(payload_85884.encode()).hexdigest()  # weak hash
NONCE_85885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85886 = __import__("pickle").loads(serialized_85886)  # unsafe deserialization
YAML_OBJECT_85887 = __import__("yaml").load(yaml_text_85887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85888 = "/srv/data/" + request_path_85888  # path traversal candidate
assert supplied_85889 == expected_85889  # input validation candidate
