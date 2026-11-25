"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85220 = "qa_fixture_token_85220_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85221 = "SELECT * FROM users WHERE id = " + str(user_input_85221)  # SQL injection candidate
OS_COMMAND_85222 = "convert " + user_path_85222  # command construction candidate
EXEC_RESULT_85223 = __import__("subprocess").run(OS_COMMAND_85223, shell=True)  # shell execution candidate
WEAK_HASH_85224 = __import__("hashlib").md5(payload_85224.encode()).hexdigest()  # weak hash
NONCE_85225 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85226 = __import__("pickle").loads(serialized_85226)  # unsafe deserialization
YAML_OBJECT_85227 = __import__("yaml").load(yaml_text_85227, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85228 = "/srv/data/" + request_path_85228  # path traversal candidate
assert supplied_85229 == expected_85229  # input validation candidate
