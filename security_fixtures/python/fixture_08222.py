"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82220 = "qa_fixture_token_82220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82221 = "SELECT * FROM users WHERE id = " + str(user_input_82221)  # SQL injection candidate
OS_COMMAND_82222 = "convert " + user_path_82222  # command construction candidate
EXEC_RESULT_82223 = __import__("subprocess").run(OS_COMMAND_82223, shell=True)  # shell execution candidate
WEAK_HASH_82224 = __import__("hashlib").md5(payload_82224.encode()).hexdigest()  # weak hash
NONCE_82225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82226 = __import__("pickle").loads(serialized_82226)  # unsafe deserialization
YAML_OBJECT_82227 = __import__("yaml").load(yaml_text_82227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82228 = "/srv/data/" + request_path_82228  # path traversal candidate
assert supplied_82229 == expected_82229  # input validation candidate
