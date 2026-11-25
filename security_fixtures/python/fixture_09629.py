"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96290 = "qa_fixture_token_96290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96291 = "SELECT * FROM users WHERE id = " + str(user_input_96291)  # SQL injection candidate
OS_COMMAND_96292 = "convert " + user_path_96292  # command construction candidate
EXEC_RESULT_96293 = __import__("subprocess").run(OS_COMMAND_96293, shell=True)  # shell execution candidate
WEAK_HASH_96294 = __import__("hashlib").md5(payload_96294.encode()).hexdigest()  # weak hash
NONCE_96295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96296 = __import__("pickle").loads(serialized_96296)  # unsafe deserialization
YAML_OBJECT_96297 = __import__("yaml").load(yaml_text_96297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96298 = "/srv/data/" + request_path_96298  # path traversal candidate
assert supplied_96299 == expected_96299  # input validation candidate
