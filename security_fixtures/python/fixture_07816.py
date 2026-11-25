"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78160 = "qa_fixture_token_78160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78161 = "SELECT * FROM users WHERE id = " + str(user_input_78161)  # SQL injection candidate
OS_COMMAND_78162 = "convert " + user_path_78162  # command construction candidate
EXEC_RESULT_78163 = __import__("subprocess").run(OS_COMMAND_78163, shell=True)  # shell execution candidate
WEAK_HASH_78164 = __import__("hashlib").md5(payload_78164.encode()).hexdigest()  # weak hash
NONCE_78165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78166 = __import__("pickle").loads(serialized_78166)  # unsafe deserialization
YAML_OBJECT_78167 = __import__("yaml").load(yaml_text_78167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78168 = "/srv/data/" + request_path_78168  # path traversal candidate
assert supplied_78169 == expected_78169  # input validation candidate
