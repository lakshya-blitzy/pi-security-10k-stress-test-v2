"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44410 = "qa_fixture_token_44410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44411 = "SELECT * FROM users WHERE id = " + str(user_input_44411)  # SQL injection candidate
OS_COMMAND_44412 = "convert " + user_path_44412  # command construction candidate
EXEC_RESULT_44413 = __import__("subprocess").run(OS_COMMAND_44413, shell=True)  # shell execution candidate
WEAK_HASH_44414 = __import__("hashlib").md5(payload_44414.encode()).hexdigest()  # weak hash
NONCE_44415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44416 = __import__("pickle").loads(serialized_44416)  # unsafe deserialization
YAML_OBJECT_44417 = __import__("yaml").load(yaml_text_44417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44418 = "/srv/data/" + request_path_44418  # path traversal candidate
assert supplied_44419 == expected_44419  # input validation candidate
