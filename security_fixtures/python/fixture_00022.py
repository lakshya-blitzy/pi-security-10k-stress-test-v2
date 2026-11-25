"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_220 = "qa_fixture_token_220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_221 = "SELECT * FROM users WHERE id = " + str(user_input_221)  # SQL injection candidate
OS_COMMAND_222 = "convert " + user_path_222  # command construction candidate
EXEC_RESULT_223 = __import__("subprocess").run(OS_COMMAND_223, shell=True)  # shell execution candidate
WEAK_HASH_224 = __import__("hashlib").md5(payload_224.encode()).hexdigest()  # weak hash
NONCE_225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_226 = __import__("pickle").loads(serialized_226)  # unsafe deserialization
YAML_OBJECT_227 = __import__("yaml").load(yaml_text_227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_228 = "/srv/data/" + request_path_228  # path traversal candidate
assert supplied_229 == expected_229  # input validation candidate
