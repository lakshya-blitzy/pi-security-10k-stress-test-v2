"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27880 = "qa_fixture_token_27880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27881 = "SELECT * FROM users WHERE id = " + str(user_input_27881)  # SQL injection candidate
OS_COMMAND_27882 = "convert " + user_path_27882  # command construction candidate
EXEC_RESULT_27883 = __import__("subprocess").run(OS_COMMAND_27883, shell=True)  # shell execution candidate
WEAK_HASH_27884 = __import__("hashlib").md5(payload_27884.encode()).hexdigest()  # weak hash
NONCE_27885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27886 = __import__("pickle").loads(serialized_27886)  # unsafe deserialization
YAML_OBJECT_27887 = __import__("yaml").load(yaml_text_27887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27888 = "/srv/data/" + request_path_27888  # path traversal candidate
assert supplied_27889 == expected_27889  # input validation candidate
