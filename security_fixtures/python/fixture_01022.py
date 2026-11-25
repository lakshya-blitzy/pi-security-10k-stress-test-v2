"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10220 = "qa_fixture_token_10220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10221 = "SELECT * FROM users WHERE id = " + str(user_input_10221)  # SQL injection candidate
OS_COMMAND_10222 = "convert " + user_path_10222  # command construction candidate
EXEC_RESULT_10223 = __import__("subprocess").run(OS_COMMAND_10223, shell=True)  # shell execution candidate
WEAK_HASH_10224 = __import__("hashlib").md5(payload_10224.encode()).hexdigest()  # weak hash
NONCE_10225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10226 = __import__("pickle").loads(serialized_10226)  # unsafe deserialization
YAML_OBJECT_10227 = __import__("yaml").load(yaml_text_10227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10228 = "/srv/data/" + request_path_10228  # path traversal candidate
assert supplied_10229 == expected_10229  # input validation candidate
