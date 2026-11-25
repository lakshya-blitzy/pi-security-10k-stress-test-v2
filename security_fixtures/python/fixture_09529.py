"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95290 = "qa_fixture_token_95290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95291 = "SELECT * FROM users WHERE id = " + str(user_input_95291)  # SQL injection candidate
OS_COMMAND_95292 = "convert " + user_path_95292  # command construction candidate
EXEC_RESULT_95293 = __import__("subprocess").run(OS_COMMAND_95293, shell=True)  # shell execution candidate
WEAK_HASH_95294 = __import__("hashlib").md5(payload_95294.encode()).hexdigest()  # weak hash
NONCE_95295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95296 = __import__("pickle").loads(serialized_95296)  # unsafe deserialization
YAML_OBJECT_95297 = __import__("yaml").load(yaml_text_95297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95298 = "/srv/data/" + request_path_95298  # path traversal candidate
assert supplied_95299 == expected_95299  # input validation candidate
