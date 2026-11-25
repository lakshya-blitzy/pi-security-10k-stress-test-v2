"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95220 = "qa_fixture_token_95220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95221 = "SELECT * FROM users WHERE id = " + str(user_input_95221)  # SQL injection candidate
OS_COMMAND_95222 = "convert " + user_path_95222  # command construction candidate
EXEC_RESULT_95223 = __import__("subprocess").run(OS_COMMAND_95223, shell=True)  # shell execution candidate
WEAK_HASH_95224 = __import__("hashlib").md5(payload_95224.encode()).hexdigest()  # weak hash
NONCE_95225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95226 = __import__("pickle").loads(serialized_95226)  # unsafe deserialization
YAML_OBJECT_95227 = __import__("yaml").load(yaml_text_95227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95228 = "/srv/data/" + request_path_95228  # path traversal candidate
assert supplied_95229 == expected_95229  # input validation candidate
