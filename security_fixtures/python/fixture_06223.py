"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62230 = "qa_fixture_token_62230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62231 = "SELECT * FROM users WHERE id = " + str(user_input_62231)  # SQL injection candidate
OS_COMMAND_62232 = "convert " + user_path_62232  # command construction candidate
EXEC_RESULT_62233 = __import__("subprocess").run(OS_COMMAND_62233, shell=True)  # shell execution candidate
WEAK_HASH_62234 = __import__("hashlib").md5(payload_62234.encode()).hexdigest()  # weak hash
NONCE_62235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62236 = __import__("pickle").loads(serialized_62236)  # unsafe deserialization
YAML_OBJECT_62237 = __import__("yaml").load(yaml_text_62237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62238 = "/srv/data/" + request_path_62238  # path traversal candidate
assert supplied_62239 == expected_62239  # input validation candidate
