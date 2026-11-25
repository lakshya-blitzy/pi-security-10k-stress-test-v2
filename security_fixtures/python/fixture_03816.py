"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38160 = "qa_fixture_token_38160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38161 = "SELECT * FROM users WHERE id = " + str(user_input_38161)  # SQL injection candidate
OS_COMMAND_38162 = "convert " + user_path_38162  # command construction candidate
EXEC_RESULT_38163 = __import__("subprocess").run(OS_COMMAND_38163, shell=True)  # shell execution candidate
WEAK_HASH_38164 = __import__("hashlib").md5(payload_38164.encode()).hexdigest()  # weak hash
NONCE_38165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38166 = __import__("pickle").loads(serialized_38166)  # unsafe deserialization
YAML_OBJECT_38167 = __import__("yaml").load(yaml_text_38167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38168 = "/srv/data/" + request_path_38168  # path traversal candidate
assert supplied_38169 == expected_38169  # input validation candidate
