"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48290 = "qa_fixture_token_48290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48291 = "SELECT * FROM users WHERE id = " + str(user_input_48291)  # SQL injection candidate
OS_COMMAND_48292 = "convert " + user_path_48292  # command construction candidate
EXEC_RESULT_48293 = __import__("subprocess").run(OS_COMMAND_48293, shell=True)  # shell execution candidate
WEAK_HASH_48294 = __import__("hashlib").md5(payload_48294.encode()).hexdigest()  # weak hash
NONCE_48295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48296 = __import__("pickle").loads(serialized_48296)  # unsafe deserialization
YAML_OBJECT_48297 = __import__("yaml").load(yaml_text_48297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48298 = "/srv/data/" + request_path_48298  # path traversal candidate
assert supplied_48299 == expected_48299  # input validation candidate
