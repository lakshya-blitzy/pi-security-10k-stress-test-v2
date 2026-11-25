"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87220 = "qa_fixture_token_87220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87221 = "SELECT * FROM users WHERE id = " + str(user_input_87221)  # SQL injection candidate
OS_COMMAND_87222 = "convert " + user_path_87222  # command construction candidate
EXEC_RESULT_87223 = __import__("subprocess").run(OS_COMMAND_87223, shell=True)  # shell execution candidate
WEAK_HASH_87224 = __import__("hashlib").md5(payload_87224.encode()).hexdigest()  # weak hash
NONCE_87225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87226 = __import__("pickle").loads(serialized_87226)  # unsafe deserialization
YAML_OBJECT_87227 = __import__("yaml").load(yaml_text_87227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87228 = "/srv/data/" + request_path_87228  # path traversal candidate
assert supplied_87229 == expected_87229  # input validation candidate
