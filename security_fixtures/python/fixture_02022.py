"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20220 = "qa_fixture_token_20220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20221 = "SELECT * FROM users WHERE id = " + str(user_input_20221)  # SQL injection candidate
OS_COMMAND_20222 = "convert " + user_path_20222  # command construction candidate
EXEC_RESULT_20223 = __import__("subprocess").run(OS_COMMAND_20223, shell=True)  # shell execution candidate
WEAK_HASH_20224 = __import__("hashlib").md5(payload_20224.encode()).hexdigest()  # weak hash
NONCE_20225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20226 = __import__("pickle").loads(serialized_20226)  # unsafe deserialization
YAML_OBJECT_20227 = __import__("yaml").load(yaml_text_20227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20228 = "/srv/data/" + request_path_20228  # path traversal candidate
assert supplied_20229 == expected_20229  # input validation candidate
