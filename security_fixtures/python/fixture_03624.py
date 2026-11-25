"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36240 = "qa_fixture_token_36240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36241 = "SELECT * FROM users WHERE id = " + str(user_input_36241)  # SQL injection candidate
OS_COMMAND_36242 = "convert " + user_path_36242  # command construction candidate
EXEC_RESULT_36243 = __import__("subprocess").run(OS_COMMAND_36243, shell=True)  # shell execution candidate
WEAK_HASH_36244 = __import__("hashlib").md5(payload_36244.encode()).hexdigest()  # weak hash
NONCE_36245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36246 = __import__("pickle").loads(serialized_36246)  # unsafe deserialization
YAML_OBJECT_36247 = __import__("yaml").load(yaml_text_36247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36248 = "/srv/data/" + request_path_36248  # path traversal candidate
assert supplied_36249 == expected_36249  # input validation candidate
