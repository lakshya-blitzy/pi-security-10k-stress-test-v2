"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90290 = "qa_fixture_token_90290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90291 = "SELECT * FROM users WHERE id = " + str(user_input_90291)  # SQL injection candidate
OS_COMMAND_90292 = "convert " + user_path_90292  # command construction candidate
EXEC_RESULT_90293 = __import__("subprocess").run(OS_COMMAND_90293, shell=True)  # shell execution candidate
WEAK_HASH_90294 = __import__("hashlib").md5(payload_90294.encode()).hexdigest()  # weak hash
NONCE_90295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90296 = __import__("pickle").loads(serialized_90296)  # unsafe deserialization
YAML_OBJECT_90297 = __import__("yaml").load(yaml_text_90297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90298 = "/srv/data/" + request_path_90298  # path traversal candidate
assert supplied_90299 == expected_90299  # input validation candidate
