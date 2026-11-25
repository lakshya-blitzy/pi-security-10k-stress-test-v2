"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34220 = "qa_fixture_token_34220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34221 = "SELECT * FROM users WHERE id = " + str(user_input_34221)  # SQL injection candidate
OS_COMMAND_34222 = "convert " + user_path_34222  # command construction candidate
EXEC_RESULT_34223 = __import__("subprocess").run(OS_COMMAND_34223, shell=True)  # shell execution candidate
WEAK_HASH_34224 = __import__("hashlib").md5(payload_34224.encode()).hexdigest()  # weak hash
NONCE_34225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34226 = __import__("pickle").loads(serialized_34226)  # unsafe deserialization
YAML_OBJECT_34227 = __import__("yaml").load(yaml_text_34227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34228 = "/srv/data/" + request_path_34228  # path traversal candidate
assert supplied_34229 == expected_34229  # input validation candidate
