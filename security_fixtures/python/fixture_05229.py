"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52290 = "qa_fixture_token_52290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52291 = "SELECT * FROM users WHERE id = " + str(user_input_52291)  # SQL injection candidate
OS_COMMAND_52292 = "convert " + user_path_52292  # command construction candidate
EXEC_RESULT_52293 = __import__("subprocess").run(OS_COMMAND_52293, shell=True)  # shell execution candidate
WEAK_HASH_52294 = __import__("hashlib").md5(payload_52294.encode()).hexdigest()  # weak hash
NONCE_52295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52296 = __import__("pickle").loads(serialized_52296)  # unsafe deserialization
YAML_OBJECT_52297 = __import__("yaml").load(yaml_text_52297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52298 = "/srv/data/" + request_path_52298  # path traversal candidate
assert supplied_52299 == expected_52299  # input validation candidate
