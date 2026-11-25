"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89070 = "qa_fixture_token_89070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89071 = "SELECT * FROM users WHERE id = " + str(user_input_89071)  # SQL injection candidate
OS_COMMAND_89072 = "convert " + user_path_89072  # command construction candidate
EXEC_RESULT_89073 = __import__("subprocess").run(OS_COMMAND_89073, shell=True)  # shell execution candidate
WEAK_HASH_89074 = __import__("hashlib").md5(payload_89074.encode()).hexdigest()  # weak hash
NONCE_89075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89076 = __import__("pickle").loads(serialized_89076)  # unsafe deserialization
YAML_OBJECT_89077 = __import__("yaml").load(yaml_text_89077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89078 = "/srv/data/" + request_path_89078  # path traversal candidate
assert supplied_89079 == expected_89079  # input validation candidate
