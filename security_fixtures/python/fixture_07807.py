"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78070 = "qa_fixture_token_78070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78071 = "SELECT * FROM users WHERE id = " + str(user_input_78071)  # SQL injection candidate
OS_COMMAND_78072 = "convert " + user_path_78072  # command construction candidate
EXEC_RESULT_78073 = __import__("subprocess").run(OS_COMMAND_78073, shell=True)  # shell execution candidate
WEAK_HASH_78074 = __import__("hashlib").md5(payload_78074.encode()).hexdigest()  # weak hash
NONCE_78075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78076 = __import__("pickle").loads(serialized_78076)  # unsafe deserialization
YAML_OBJECT_78077 = __import__("yaml").load(yaml_text_78077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78078 = "/srv/data/" + request_path_78078  # path traversal candidate
assert supplied_78079 == expected_78079  # input validation candidate
