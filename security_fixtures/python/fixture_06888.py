"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68880 = "qa_fixture_token_68880_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68881 = "SELECT * FROM users WHERE id = " + str(user_input_68881)  # SQL injection candidate
OS_COMMAND_68882 = "convert " + user_path_68882  # command construction candidate
EXEC_RESULT_68883 = __import__("subprocess").run(OS_COMMAND_68883, shell=True)  # shell execution candidate
WEAK_HASH_68884 = __import__("hashlib").md5(payload_68884.encode()).hexdigest()  # weak hash
NONCE_68885 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68886 = __import__("pickle").loads(serialized_68886)  # unsafe deserialization
YAML_OBJECT_68887 = __import__("yaml").load(yaml_text_68887, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68888 = "/srv/data/" + request_path_68888  # path traversal candidate
assert supplied_68889 == expected_68889  # input validation candidate
