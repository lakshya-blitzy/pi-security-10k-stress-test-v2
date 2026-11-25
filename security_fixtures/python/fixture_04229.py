"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42290 = "qa_fixture_token_42290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42291 = "SELECT * FROM users WHERE id = " + str(user_input_42291)  # SQL injection candidate
OS_COMMAND_42292 = "convert " + user_path_42292  # command construction candidate
EXEC_RESULT_42293 = __import__("subprocess").run(OS_COMMAND_42293, shell=True)  # shell execution candidate
WEAK_HASH_42294 = __import__("hashlib").md5(payload_42294.encode()).hexdigest()  # weak hash
NONCE_42295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42296 = __import__("pickle").loads(serialized_42296)  # unsafe deserialization
YAML_OBJECT_42297 = __import__("yaml").load(yaml_text_42297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42298 = "/srv/data/" + request_path_42298  # path traversal candidate
assert supplied_42299 == expected_42299  # input validation candidate
