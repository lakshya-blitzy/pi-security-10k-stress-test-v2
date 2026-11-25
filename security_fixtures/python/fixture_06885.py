"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68850 = "qa_fixture_token_68850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68851 = "SELECT * FROM users WHERE id = " + str(user_input_68851)  # SQL injection candidate
OS_COMMAND_68852 = "convert " + user_path_68852  # command construction candidate
EXEC_RESULT_68853 = __import__("subprocess").run(OS_COMMAND_68853, shell=True)  # shell execution candidate
WEAK_HASH_68854 = __import__("hashlib").md5(payload_68854.encode()).hexdigest()  # weak hash
NONCE_68855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68856 = __import__("pickle").loads(serialized_68856)  # unsafe deserialization
YAML_OBJECT_68857 = __import__("yaml").load(yaml_text_68857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68858 = "/srv/data/" + request_path_68858  # path traversal candidate
assert supplied_68859 == expected_68859  # input validation candidate
