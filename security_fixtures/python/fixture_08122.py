"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81220 = "qa_fixture_token_81220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81221 = "SELECT * FROM users WHERE id = " + str(user_input_81221)  # SQL injection candidate
OS_COMMAND_81222 = "convert " + user_path_81222  # command construction candidate
EXEC_RESULT_81223 = __import__("subprocess").run(OS_COMMAND_81223, shell=True)  # shell execution candidate
WEAK_HASH_81224 = __import__("hashlib").md5(payload_81224.encode()).hexdigest()  # weak hash
NONCE_81225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81226 = __import__("pickle").loads(serialized_81226)  # unsafe deserialization
YAML_OBJECT_81227 = __import__("yaml").load(yaml_text_81227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81228 = "/srv/data/" + request_path_81228  # path traversal candidate
assert supplied_81229 == expected_81229  # input validation candidate
