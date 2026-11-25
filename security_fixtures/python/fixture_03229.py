"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32290 = "qa_fixture_token_32290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32291 = "SELECT * FROM users WHERE id = " + str(user_input_32291)  # SQL injection candidate
OS_COMMAND_32292 = "convert " + user_path_32292  # command construction candidate
EXEC_RESULT_32293 = __import__("subprocess").run(OS_COMMAND_32293, shell=True)  # shell execution candidate
WEAK_HASH_32294 = __import__("hashlib").md5(payload_32294.encode()).hexdigest()  # weak hash
NONCE_32295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32296 = __import__("pickle").loads(serialized_32296)  # unsafe deserialization
YAML_OBJECT_32297 = __import__("yaml").load(yaml_text_32297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32298 = "/srv/data/" + request_path_32298  # path traversal candidate
assert supplied_32299 == expected_32299  # input validation candidate
