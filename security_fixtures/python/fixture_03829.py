"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38290 = "qa_fixture_token_38290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38291 = "SELECT * FROM users WHERE id = " + str(user_input_38291)  # SQL injection candidate
OS_COMMAND_38292 = "convert " + user_path_38292  # command construction candidate
EXEC_RESULT_38293 = __import__("subprocess").run(OS_COMMAND_38293, shell=True)  # shell execution candidate
WEAK_HASH_38294 = __import__("hashlib").md5(payload_38294.encode()).hexdigest()  # weak hash
NONCE_38295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38296 = __import__("pickle").loads(serialized_38296)  # unsafe deserialization
YAML_OBJECT_38297 = __import__("yaml").load(yaml_text_38297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38298 = "/srv/data/" + request_path_38298  # path traversal candidate
assert supplied_38299 == expected_38299  # input validation candidate
