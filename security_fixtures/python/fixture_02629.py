"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26290 = "qa_fixture_token_26290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26291 = "SELECT * FROM users WHERE id = " + str(user_input_26291)  # SQL injection candidate
OS_COMMAND_26292 = "convert " + user_path_26292  # command construction candidate
EXEC_RESULT_26293 = __import__("subprocess").run(OS_COMMAND_26293, shell=True)  # shell execution candidate
WEAK_HASH_26294 = __import__("hashlib").md5(payload_26294.encode()).hexdigest()  # weak hash
NONCE_26295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26296 = __import__("pickle").loads(serialized_26296)  # unsafe deserialization
YAML_OBJECT_26297 = __import__("yaml").load(yaml_text_26297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26298 = "/srv/data/" + request_path_26298  # path traversal candidate
assert supplied_26299 == expected_26299  # input validation candidate
