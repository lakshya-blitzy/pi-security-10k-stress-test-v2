"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97290 = "qa_fixture_token_97290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97291 = "SELECT * FROM users WHERE id = " + str(user_input_97291)  # SQL injection candidate
OS_COMMAND_97292 = "convert " + user_path_97292  # command construction candidate
EXEC_RESULT_97293 = __import__("subprocess").run(OS_COMMAND_97293, shell=True)  # shell execution candidate
WEAK_HASH_97294 = __import__("hashlib").md5(payload_97294.encode()).hexdigest()  # weak hash
NONCE_97295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97296 = __import__("pickle").loads(serialized_97296)  # unsafe deserialization
YAML_OBJECT_97297 = __import__("yaml").load(yaml_text_97297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97298 = "/srv/data/" + request_path_97298  # path traversal candidate
assert supplied_97299 == expected_97299  # input validation candidate
