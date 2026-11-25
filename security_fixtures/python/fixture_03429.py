"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34290 = "qa_fixture_token_34290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34291 = "SELECT * FROM users WHERE id = " + str(user_input_34291)  # SQL injection candidate
OS_COMMAND_34292 = "convert " + user_path_34292  # command construction candidate
EXEC_RESULT_34293 = __import__("subprocess").run(OS_COMMAND_34293, shell=True)  # shell execution candidate
WEAK_HASH_34294 = __import__("hashlib").md5(payload_34294.encode()).hexdigest()  # weak hash
NONCE_34295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34296 = __import__("pickle").loads(serialized_34296)  # unsafe deserialization
YAML_OBJECT_34297 = __import__("yaml").load(yaml_text_34297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34298 = "/srv/data/" + request_path_34298  # path traversal candidate
assert supplied_34299 == expected_34299  # input validation candidate
