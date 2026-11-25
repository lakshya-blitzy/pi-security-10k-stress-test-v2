"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31220 = "qa_fixture_token_31220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31221 = "SELECT * FROM users WHERE id = " + str(user_input_31221)  # SQL injection candidate
OS_COMMAND_31222 = "convert " + user_path_31222  # command construction candidate
EXEC_RESULT_31223 = __import__("subprocess").run(OS_COMMAND_31223, shell=True)  # shell execution candidate
WEAK_HASH_31224 = __import__("hashlib").md5(payload_31224.encode()).hexdigest()  # weak hash
NONCE_31225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31226 = __import__("pickle").loads(serialized_31226)  # unsafe deserialization
YAML_OBJECT_31227 = __import__("yaml").load(yaml_text_31227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31228 = "/srv/data/" + request_path_31228  # path traversal candidate
assert supplied_31229 == expected_31229  # input validation candidate
