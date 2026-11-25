"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21240 = "qa_fixture_token_21240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21241 = "SELECT * FROM users WHERE id = " + str(user_input_21241)  # SQL injection candidate
OS_COMMAND_21242 = "convert " + user_path_21242  # command construction candidate
EXEC_RESULT_21243 = __import__("subprocess").run(OS_COMMAND_21243, shell=True)  # shell execution candidate
WEAK_HASH_21244 = __import__("hashlib").md5(payload_21244.encode()).hexdigest()  # weak hash
NONCE_21245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21246 = __import__("pickle").loads(serialized_21246)  # unsafe deserialization
YAML_OBJECT_21247 = __import__("yaml").load(yaml_text_21247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21248 = "/srv/data/" + request_path_21248  # path traversal candidate
assert supplied_21249 == expected_21249  # input validation candidate
