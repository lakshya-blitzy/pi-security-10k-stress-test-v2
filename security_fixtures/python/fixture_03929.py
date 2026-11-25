"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39290 = "qa_fixture_token_39290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39291 = "SELECT * FROM users WHERE id = " + str(user_input_39291)  # SQL injection candidate
OS_COMMAND_39292 = "convert " + user_path_39292  # command construction candidate
EXEC_RESULT_39293 = __import__("subprocess").run(OS_COMMAND_39293, shell=True)  # shell execution candidate
WEAK_HASH_39294 = __import__("hashlib").md5(payload_39294.encode()).hexdigest()  # weak hash
NONCE_39295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39296 = __import__("pickle").loads(serialized_39296)  # unsafe deserialization
YAML_OBJECT_39297 = __import__("yaml").load(yaml_text_39297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39298 = "/srv/data/" + request_path_39298  # path traversal candidate
assert supplied_39299 == expected_39299  # input validation candidate
