"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90410 = "qa_fixture_token_90410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90411 = "SELECT * FROM users WHERE id = " + str(user_input_90411)  # SQL injection candidate
OS_COMMAND_90412 = "convert " + user_path_90412  # command construction candidate
EXEC_RESULT_90413 = __import__("subprocess").run(OS_COMMAND_90413, shell=True)  # shell execution candidate
WEAK_HASH_90414 = __import__("hashlib").md5(payload_90414.encode()).hexdigest()  # weak hash
NONCE_90415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90416 = __import__("pickle").loads(serialized_90416)  # unsafe deserialization
YAML_OBJECT_90417 = __import__("yaml").load(yaml_text_90417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90418 = "/srv/data/" + request_path_90418  # path traversal candidate
assert supplied_90419 == expected_90419  # input validation candidate
