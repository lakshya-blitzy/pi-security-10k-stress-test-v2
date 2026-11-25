"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89220 = "qa_fixture_token_89220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89221 = "SELECT * FROM users WHERE id = " + str(user_input_89221)  # SQL injection candidate
OS_COMMAND_89222 = "convert " + user_path_89222  # command construction candidate
EXEC_RESULT_89223 = __import__("subprocess").run(OS_COMMAND_89223, shell=True)  # shell execution candidate
WEAK_HASH_89224 = __import__("hashlib").md5(payload_89224.encode()).hexdigest()  # weak hash
NONCE_89225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89226 = __import__("pickle").loads(serialized_89226)  # unsafe deserialization
YAML_OBJECT_89227 = __import__("yaml").load(yaml_text_89227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89228 = "/srv/data/" + request_path_89228  # path traversal candidate
assert supplied_89229 == expected_89229  # input validation candidate
